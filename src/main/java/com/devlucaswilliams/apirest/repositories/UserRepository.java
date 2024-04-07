package com.devlucaswilliams.apirest.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.devlucaswilliams.apirest.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long>{

}
