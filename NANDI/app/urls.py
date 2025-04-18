from django.urls import path
from .views import *    
urlpatterns = [
    # Report
    path('report_gallary', rgallary ,name='report_gallary'),
    path('customer_report', customer_report ,name='customer_report'),
    path('payment_report', payment_report ,name='payment_report'),
    path('Booking_report', Booking_report ,name='Booking_report'),
    path('Executve_report', Executve_report ,name='Executve_report'),
    path('manager_report', manager_report ,name='manager_report'),
    path('Tellicaller_report', Tellicaller_report ,name='Tellicaller_report'),
    # Store Master
    path('t_delete/<int:id>',t_delete,name='t_delete'),
    path('t_edit/<int:id>',t_edit,name='t_edit'),
    path('t_add',t_add,name='t_add'),
    path('t_list',t_list,name='t_list'),
    path('m_delete/<int:id>',m_delete,name='m_delete'),
    path('m_edit/<int:id>',m_edit,name='m_edit'),
    path('m_add',m_add,name='m_add'),
    path('m_list',m_list,name='m_list'),
    path('ex_delete/<int:id>',ex_delete,name='ex_delete'),
    path('ex_edit/<int:id>',ex_edit,name='ex_edit'),
    path('ex_add', ex_add ,name='ex_add'),
    path('ex_list', ex_list ,name='ex_list'),
    path('project_delete/<int:id>',project_delete,name='project_delete'),
    path('project_edit/<int:id>',project_edit,name='project_edit'),
    path('project_add',project_add,name='project_add'),
    path('project_list',project_list,name='project_list'),
    # Call Back
    path('call_back',call_back,name="call_back"),
    # Agreement
    path('nandi_flat',nandi_flat,name='nandi_flat'),
    path('nandi_plot',nandi_plot,name='nandi_plot'),
    path('viewpage',viewpage,name="viewpage"),
    # incentive
    path('incetive_executive',incetive_executive,name='incetive_executive'),
    path('ex_pay_add',ex_pay_add,name='ex_pay_add'),
    path('ex_pay_edit/<int:id>',ex_pay_edit,name='ex_pay_edit'),
    path('m_pay_add',m_pay_add,name='m_pay_add'),
    path('m_pay_edit/<int:id>',m_pay_edit,name='m_pay_edit'),
    path('incetive_manager',incetive_manager,name='incetive_manager'),
    path('t_pay_add',t_pay_add,name='t_pay_add'),
    path('t_pay_edit/<int:id>',t_pay_edit,name='t_pay_edit'),
    path('incentive_tellicaller',incentive_tellicaller,name='incentive_tellicaller'),
    # Follow Up
    path('follow_up',follow_up,name='follow_up'),
    # Payment
    path('ledger',ledger,name='ledger'),
    path('pay_edit/<int:id>',pay_edit,name='pay_edit'),
    path('pay_add',pay_add,name='pay_add'),
    path('pay_view',pay_view,name='pay_view'),
    path('reciept_list',reciept_list,name='reciept_list'),
    path('A_list',A_list,name='A_list'),
    path('Approval_permit/<int:id>',Approval_permit,name='Approval_permit'),
    path('ledger_view/<int:id>',ledger_view,name='ledger_view'),
    #  Booking
    path('Booking_delete/<int:id>',Booking_delete,name='Booking_delete'),
    path('Booking_edit/<int:id>',Booking_edit,name='Booking_edit'),
    path('booking_view/<int:id>',booking_view,name='booking_view'),
    path('Booking_add',Booking_add,name='Booking_add'),
    path('Booking_list',Booking_list,name='Booking_list'),    
    # Customer
    path('customer_delete/<int:id>',customer_delete,name='customer_delete'),
    path('customer_edit/<int:id>',customer_edit,name='customer_edit'),
    path('customer_add',customer_add,name='customer_add'),
    path('customer_list',customer_list,name='customer_list'),
    path('home',home,name='home'),
    path('logout',Logout,name='logout'),
    path('',Loginuser,name='login'),
]
