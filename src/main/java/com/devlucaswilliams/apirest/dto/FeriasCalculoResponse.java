package com.devlucaswilliams.apirest.dto;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class FeriasCalculoResponse {

	private BigDecimal salarioMensal;
	private int totalDias;
	private BigDecimal valorDia;
	private List<PeriodoFeriasValor> periodos = new ArrayList<>();
	private BigDecimal totalJaRecebido;
	private BigDecimal totalAReceberAgora;
	private BigDecimal totalAReceberEmJaneiro;
	private BigDecimal totalGeral;
	private String resumo;

	public FeriasCalculoResponse() {
	}

	public BigDecimal getSalarioMensal() {
		return salarioMensal;
	}

	public void setSalarioMensal(BigDecimal salarioMensal) {
		this.salarioMensal = salarioMensal;
	}

	public int getTotalDias() {
		return totalDias;
	}

	public void setTotalDias(int totalDias) {
		this.totalDias = totalDias;
	}

	public BigDecimal getValorDia() {
		return valorDia;
	}

	public void setValorDia(BigDecimal valorDia) {
		this.valorDia = valorDia;
	}

	public List<PeriodoFeriasValor> getPeriodos() {
		return periodos;
	}

	public void setPeriodos(List<PeriodoFeriasValor> periodos) {
		this.periodos = periodos;
	}

	public BigDecimal getTotalJaRecebido() {
		return totalJaRecebido;
	}

	public void setTotalJaRecebido(BigDecimal totalJaRecebido) {
		this.totalJaRecebido = totalJaRecebido;
	}

	public BigDecimal getTotalAReceberAgora() {
		return totalAReceberAgora;
	}

	public void setTotalAReceberAgora(BigDecimal totalAReceberAgora) {
		this.totalAReceberAgora = totalAReceberAgora;
	}

	public BigDecimal getTotalAReceberEmJaneiro() {
		return totalAReceberEmJaneiro;
	}

	public void setTotalAReceberEmJaneiro(BigDecimal totalAReceberEmJaneiro) {
		this.totalAReceberEmJaneiro = totalAReceberEmJaneiro;
	}

	public BigDecimal getTotalGeral() {
		return totalGeral;
	}

	public void setTotalGeral(BigDecimal totalGeral) {
		this.totalGeral = totalGeral;
	}

	public String getResumo() {
		return resumo;
	}

	public void setResumo(String resumo) {
		this.resumo = resumo;
	}
}
