package com.devlucaswilliams.apirest.dto;

import java.math.BigDecimal;

/**
 * Request para calcular o valor das férias fracionadas.
 * Exemplo: 15 dias já tirados, 5 agora e 10 em janeiro.
 */
public class FeriasCalculoRequest {

	private BigDecimal salarioMensal;
	private int diasJaTirados;
	private int diasAgora;
	private int diasJaneiro;

	public FeriasCalculoRequest() {
	}

	public FeriasCalculoRequest(BigDecimal salarioMensal, int diasJaTirados, int diasAgora, int diasJaneiro) {
		this.salarioMensal = salarioMensal;
		this.diasJaTirados = diasJaTirados;
		this.diasAgora = diasAgora;
		this.diasJaneiro = diasJaneiro;
	}

	public BigDecimal getSalarioMensal() {
		return salarioMensal;
	}

	public void setSalarioMensal(BigDecimal salarioMensal) {
		this.salarioMensal = salarioMensal;
	}

	public int getDiasJaTirados() {
		return diasJaTirados;
	}

	public void setDiasJaTirados(int diasJaTirados) {
		this.diasJaTirados = diasJaTirados;
	}

	public int getDiasAgora() {
		return diasAgora;
	}

	public void setDiasAgora(int diasAgora) {
		this.diasAgora = diasAgora;
	}

	public int getDiasJaneiro() {
		return diasJaneiro;
	}

	public void setDiasJaneiro(int diasJaneiro) {
		this.diasJaneiro = diasJaneiro;
	}
}
