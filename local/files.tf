resource "local_file" "steak" {
    
   # filename = var.file_name
    content = var.file_data
    filename = "${path.module}/foo.bar"
      
}