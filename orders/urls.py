from django.urls import path
from orders import views

urlpatterns = [
    # Lấy danh sách và tạo đơn hàng
    path(
        "orders/",
        views.OrderAPIView.as_view()
    ),

    # Xem, sửa, xóa một đơn hàng
    path(
        "orders/<slug:id_slug>/",
        views.OrderDetailAPIView.as_view()
    ),

    # Lấy danh sách và thêm sản phẩm vào đơn hàng
    path(
        "orders/<slug:order_id_slug>/detail/",
        views.OrderDetailWithProductAPIView.as_view()
    ),

    # Xem, sửa, xóa một sản phẩm trong đơn hàng
    path(
        "orders/<slug:order_id_slug>/detail/<slug:id_slug>/",
        views.OrderDetailWithProductDetailAPIView.as_view()
    ),
]