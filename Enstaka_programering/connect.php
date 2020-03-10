<?php
$servername = "localhost";
$username = "grupptre";
$password = "trampulingitarr";
$databas = "grupptre";

// Create connection
$conn = new mysqli($servername, $username, $password, $databas);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "";
?>