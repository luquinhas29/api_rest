package com.devlucaswilliams.apirest.services;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.math.BigDecimal;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.devlucaswilliams.apirest.dto.FeriasCalculoRequest;
import com.devlucaswilliams.apirest.dto.FeriasCalculoResponse;

class FeriasCalculoServiceTest {

	private FeriasCalculoService service;

	@BeforeEach
	void setUp() {
		service = new FeriasCalculoService();
	}

	@Test
	void deveCalcularCenarioQuinzeCincoEDez() {
		FeriasCalculoRequest request = new FeriasCalculoRequest(
				new BigDecimal("3000.00"), 15, 5, 10);

		FeriasCalculoResponse response = service.calcular(request);

		assertEquals(30, response.getTotalDias());
		// 15 dias: 1500 + 500 = 2000
		assertEquals(new BigDecimal("2000.00"), response.getTotalJaRecebido());
		// 5 dias: 500 + 166.67 = 666.67
		assertEquals(new BigDecimal("666.67"), response.getTotalAReceberAgora());
		// 10 dias: 1000 + 333.33 = 1333.33
		assertEquals(new BigDecimal("1333.33"), response.getTotalAReceberEmJaneiro());
		assertEquals(new BigDecimal("4000.00"), response.getTotalGeral());
		assertTrue(response.getResumo().contains("já recebeu"));
		assertTrue(response.getResumo().contains("agora"));
		assertTrue(response.getResumo().contains("janeiro"));
	}

	@Test
	void deveRejeitarSalarioInvalido() {
		FeriasCalculoRequest request = new FeriasCalculoRequest(BigDecimal.ZERO, 15, 5, 10);
		assertThrows(IllegalArgumentException.class, () -> service.calcular(request));
	}

	@Test
	void deveRejeitarMaisDeTrintaDias() {
		FeriasCalculoRequest request = new FeriasCalculoRequest(
				new BigDecimal("2500.00"), 20, 10, 5);
		assertThrows(IllegalArgumentException.class, () -> service.calcular(request));
	}
}
