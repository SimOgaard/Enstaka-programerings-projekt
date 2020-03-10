<?php
include ("connect.php");

$Id = $_GET["Id"]:
$Tempratur = $_GET["Tempratur"];
$Fukt = $_GET["Fukt"]

$sql = "INSERT INTO simon (Id, Tempratur, Fukt, Tid)
VALUES ('$Id', '$Tempratur', '$Fukt')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully<br>".$Tempratur." and ".$Fukt." was added";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>