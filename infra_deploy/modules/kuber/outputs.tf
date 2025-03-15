# output "external_ip_address" {
#   value = yandex_compute_instance.vm.network_interface.0.nat_ip_address
# }

output "cluster_id" {
  value = yandex_kubernetes_cluster.k8s_cluster.id
}
