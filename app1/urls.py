from django.urls import path
from . import views as v


urlpatterns = [
    path('',v.Login,name='Login'),
    path('Register/',v.Register,name='Register'),
    path('Dashboard/',v.Dashboard,name='Dashboard'),
    path('Logout/',v.Logout,name='Logout'),
    path('Profile/',v.Profile,name='Profile'),
    path('View/',v.View_cus,name='View_cus'),
    path('Add/',v.Add_cus,name='Add_cus'),
    path('Del/<int:id>',v.Del_Cus,name='Del_Cus'),
    path('Cu_login/',v.cu_login,name='cu_login'),
    path('Cu_Logout/',v.cu_Logout,name='cu_Logout'),
   # path('Cu_dash/',v.cu_dash,name='cu_dash'),
    path('Cu_Home/',v.cu_Home,name='cu_Home'),
    path('Cu_Profile/',v.Cu_Profile,name='Cu_Profile'),
    path('AddProduct/',v.AddProduct,name='AddProduct'),
    path('ViewProduct/',v.ViewProduct,name='ViewProduct'),
    path('DeleteProduct/<int:id>',v.DeleteProduct,name='DeleteProduct'),
    path('UpdateProduct/<int:id>',v.UpdateProduct,name='UpdateProduct'),
    path('Order/<int:id>',v.order_place,name='order_place'),
    path('view Order/',v.view_order,name='view_order'),
    path('YEsOrder/<int:id>',v.YEsOrder,name='YEsOrder'),
    path('NoOrder/<int:id>',v.NoOrder,name='NoOrder'),
    path('Moreinfo/<int:id>',v.Moreinfo,name='Moreinfo'),
    path('About/',v.About,name='About'),
    path('pending/',v.pending,name='pending'),
    path('accept/',v.accept,name='accept'),
    path('cancel/',v.cancel,name='cancel'),
    path('notice',v.notice,name='notice'),
]