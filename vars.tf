variable "engine" {}
variable "engine_version" {}
variable "instance_class" {}
variable "db_name" {}
variable "username" {}
variable "parameter_group_name" {}
variable "password" {
    description = "RDS user password"
    type        = string
    sensitive   = true

}
