package com.devlucaswilliams.apirest.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.devlucaswilliams.apirest.dto.FeriasCalculoRequest;
import com.devlucaswilliams.apirest.dto.FeriasCalculoResponse;
import com.devlucaswilliams.apirest.services.FeriasCalculoService;

import java.util.Map;

@RestController
@RequestMapping(value = "/ferias")
public class FeriasController {

	@Autowired
	private FeriasCalculoService service;

	/**
	 * Calcula quanto você recebe das férias fracionadas.
	 *
	 * Exemplo de body:
	 * {
	 *   "salarioMensal": 3000.00,
	 *   "diasJaTirados": 15,
	 *   "diasAgora": 5,
	 *   "diasJaneiro": 10
	 * }
	 */
	@PostMapping(value = "/calcular")
	public FeriasCalculoResponse calcular(@RequestBody FeriasCalculoRequest request) {
		return service.calcular(request);
	}

	@ExceptionHandler(IllegalArgumentException.class)
	public ResponseEntity<Map<String, String>> handleValidation(IllegalArgumentException ex) {
		return ResponseEntity.status(HttpStatus.BAD_REQUEST)
				.body(Map.of("erro", ex.getMessage()));
	}
}
