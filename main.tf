resource "aws_db_instance" "rds" {
    allocated_storage       = 10
    engine                  = var.engine
    engine_version          = var.engine_version
    instance_class          = var.instance_class
    db_name                 = var.db_name

    username                = var.username
    password                = var.password
    parameter_group_name    = var.parameter_group_name
    publicly_accessible     = true
    skip_final_snapshot     = true
}