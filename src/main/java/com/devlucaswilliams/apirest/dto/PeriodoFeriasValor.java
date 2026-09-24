package com.devlucaswilliams.apirest.dto;

import java.math.BigDecimal;

public class PeriodoFeriasValor {

	private String descricao;
	private int dias;
	private BigDecimal valorProporcional;
	private BigDecimal tercoConstitucional;
	private BigDecimal total;
	private String status;

	public PeriodoFeriasValor() {
	}

	public PeriodoFeriasValor(String descricao, int dias, BigDecimal valorProporcional,
			BigDecimal tercoConstitucional, BigDecimal total, String status) {
		this.descricao = descricao;
		this.dias = dias;
		this.valorProporcional = valorProporcional;
		this.tercoConstitucional = tercoConstitucional;
		this.total = total;
		this.status = status;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public int getDias() {
		return dias;
	}

	public void setDias(int dias) {
		this.dias = dias;
	}

	public BigDecimal getValorProporcional() {
		return valorProporcional;
	}

	public void setValorProporcional(BigDecimal valorProporcional) {
		this.valorProporcional = valorProporcional;
	}

	public BigDecimal getTercoConstitucional() {
		return tercoConstitucional;
	}

	public void setTercoConstitucional(BigDecimal tercoConstitucional) {
		this.tercoConstitucional = tercoConstitucional;
	}

	public BigDecimal getTotal() {
		return total;
	}

	public void setTotal(BigDecimal total) {
		this.total = total;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}
}
