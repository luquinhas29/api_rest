package com.devlucaswilliams.apirest.services;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import java.util.Locale;

import org.springframework.stereotype.Service;

import com.devlucaswilliams.apirest.dto.FeriasCalculoRequest;
import com.devlucaswilliams.apirest.dto.FeriasCalculoResponse;
import com.devlucaswilliams.apirest.dto.PeriodoFeriasValor;

/**
 * Calcula férias conforme a CLT: (salário / 30 × dias) + 1/3 constitucional.
 */
@Service
public class FeriasCalculoService {

	private static final int DIAS_MES = 30;
	private static final int DIAS_FERIAS_ANO = 30;
	private static final BigDecimal TERCO = new BigDecimal("3");
	private static final Locale PT_BR = Locale.forLanguageTag("pt-BR");

	public FeriasCalculoResponse calcular(FeriasCalculoRequest request) {
		validar(request);

		BigDecimal salario = request.getSalarioMensal().setScale(2, RoundingMode.HALF_UP);
		BigDecimal valorDia = salario.divide(BigDecimal.valueOf(DIAS_MES), 4, RoundingMode.HALF_UP);

		PeriodoFeriasValor jaTirados = montarPeriodo(
				"Já tiradas",
				request.getDiasJaTirados(),
				valorDia,
				"JA_RECEBIDO");
		PeriodoFeriasValor agora = montarPeriodo(
				"Agora (próximo gozo)",
				request.getDiasAgora(),
				valorDia,
				"A_RECEBER_AGORA");
		PeriodoFeriasValor janeiro = montarPeriodo(
				"Janeiro",
				request.getDiasJaneiro(),
				valorDia,
				"A_RECEBER_EM_JANEIRO");

		int totalDias = request.getDiasJaTirados() + request.getDiasAgora() + request.getDiasJaneiro();

		FeriasCalculoResponse response = new FeriasCalculoResponse();
		response.setSalarioMensal(salario);
		response.setTotalDias(totalDias);
		response.setValorDia(valorDia.setScale(2, RoundingMode.HALF_UP));
		response.getPeriodos().add(jaTirados);
		response.getPeriodos().add(agora);
		response.getPeriodos().add(janeiro);
		response.setTotalJaRecebido(jaTirados.getTotal());
		response.setTotalAReceberAgora(agora.getTotal());
		response.setTotalAReceberEmJaneiro(janeiro.getTotal());
		response.setTotalGeral(jaTirados.getTotal().add(agora.getTotal()).add(janeiro.getTotal()));
		response.setResumo(montarResumo(response));
		return response;
	}

	private PeriodoFeriasValor montarPeriodo(String descricao, int dias, BigDecimal valorDia, String status) {
		BigDecimal proporcional = valorDia
				.multiply(BigDecimal.valueOf(dias))
				.setScale(2, RoundingMode.HALF_UP);
		BigDecimal terco = proporcional
				.divide(TERCO, 2, RoundingMode.HALF_UP);
		BigDecimal total = proporcional.add(terco);
		return new PeriodoFeriasValor(descricao, dias, proporcional, terco, total, status);
	}

	private void validar(FeriasCalculoRequest request) {
		if (request.getSalarioMensal() == null || request.getSalarioMensal().compareTo(BigDecimal.ZERO) <= 0) {
			throw new IllegalArgumentException("Informe um salário mensal maior que zero.");
		}
		if (request.getDiasJaTirados() < 0 || request.getDiasAgora() < 0 || request.getDiasJaneiro() < 0) {
			throw new IllegalArgumentException("A quantidade de dias não pode ser negativa.");
		}
		int total = request.getDiasJaTirados() + request.getDiasAgora() + request.getDiasJaneiro();
		if (total == 0) {
			throw new IllegalArgumentException("Informe ao menos um período com dias de férias.");
		}
		if (total > DIAS_FERIAS_ANO) {
			throw new IllegalArgumentException(
					"A soma dos períodos (" + total + ") não pode ultrapassar " + DIAS_FERIAS_ANO + " dias.");
		}
	}

	private String montarResumo(FeriasCalculoResponse response) {
		NumberFormat moeda = NumberFormat.getCurrencyInstance(PT_BR);
		return String.format(
				"Com salário de %s: você já recebeu %s pelos %d dias tirados; "
						+ "vai receber %s pelos %d dias agora; "
						+ "e %s pelos %d dias de janeiro. Total geral das férias: %s.",
				moeda.format(response.getSalarioMensal()),
				moeda.format(response.getTotalJaRecebido()),
				response.getPeriodos().get(0).getDias(),
				moeda.format(response.getTotalAReceberAgora()),
				response.getPeriodos().get(1).getDias(),
				moeda.format(response.getTotalAReceberEmJaneiro()),
				response.getPeriodos().get(2).getDias(),
				moeda.format(response.getTotalGeral()));
	}
}
