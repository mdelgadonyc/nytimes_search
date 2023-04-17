output "rds_hostname" {
    description = "The address of the RDS instance"
    value       = aws_db_instance.rds.address
}

output "rds_port" {
    description = "RDS instance port"
    value       = aws_db_instance.rds.port
    #sensitive   = true
}

output "rds_username" {
    description = "RDS instance root username"
    value       = aws_db_instance.rds.username
    #sensitive   = true
}