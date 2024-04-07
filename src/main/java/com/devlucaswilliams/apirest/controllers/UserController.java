package com.devlucaswilliams.apirest.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.devlucaswilliams.apirest.entities.User;
import com.devlucaswilliams.apirest.repositories.UserRepository;

@RestController
@RequestMapping(value = "/users")
public class UserController {
	
	@Autowired
	private UserRepository repository;
	
	@GetMapping
	public List<User> findAll(){
		List<User> user = repository.findAll();
		return user;
	}
	
	@GetMapping(value = "/{id}")
	public User findById(@PathVariable Long id){
		User user = repository.findById(id).get();
		return user;
	}
	
	@PostMapping
	public User inset(@RequestBody User entity){
		User user = repository.save(entity);
		return user;
	}

}
