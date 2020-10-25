from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .DBHelper import DBHelper

def index(request):
    return render(request, 'index.html')


def ReportListAllReceipts(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT r.receipt_no as "Receipt No", r.date as "Date" '
                              ' , r.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , r.payment_code as "Payment Method", r.payment_ref as "Payment Reference" '
                              ' , r.remarks as "Remarks", r.total_received as "Total Received"'
                              ' , rli.invoice_no as "Invoice No"'
                              ' , i.date as "Invoice Date", rli.amount_paid_here as "Amount Paid Here"'
                              '  FROM receipt r '
                              '  JOIN customer c ON r.customer_code = c.customer_code '
                              '  JOIN receipt_line_item rli ON r.receipt_no = rli.receipt_no '
                              '  JOIN invoice i ON rli.invoice_no = i.invoice_no ')

    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns

    return render(request, 'report_list_all_receipts.html', data_report)

def ReportUnpaidInvoices(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT "Invoice No", i.date as "Invoice Date" '
		                     '  , c.name as "Customer Name", i.amount_due AS "Invoice Amount Due" '
		                     '  , "Invoice Amount Received", i.amount_due - "Invoice Amount Received" AS "Invoice Amount Not Paid" '
                             ' FROM( SELECT rli.invoice_no as "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received" '
	                         '  FROM receipt_line_item as rli '
	                         '  GROUP BY rli.invoice_no ) as li '
                             '  JOIN invoice as i '
	                         '   ON li."Invoice No" = i.invoice_no '
                             ' INNER JOIN customer as c '
	                         '   ON i.customer_code = c.customer_code')

    data1, columns1 = db.fetch ('SELECT SUM(i.amount_due - "Invoice Amount Received") AS "Total Dept" '
                              'FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received" '
	                          '  FROM receipt_line_item as rli '
	                          ' GROUP BY rli.invoice_no ) as li '
                              ' INNER JOIN invoice as i '
	                          '  ON li."Invoice No" = i.invoice_no ')
    
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['data1'] = CursorToDict (data1,columns1)
    data_report['column_name'] = columns

    return render(request, 'report_unpaid_invoice.html', data_report)

def ReportDateAmountReceived(request):
    db = DBHelper()
    data, columns = db.fetch (' SELECT "Date", "Customer Name", "Invoice Amount Received" '
                              ' FROM(SELECT i.date as "Date", c.customer_code as "Customer Code", c.name as "Customer Name", '
		                      ' i.invoice_no as "Invoice No","Invoice Amount Received" '
		                      ' FROM (SELECT rli.invoice_no as "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received" '
	  		                  ' FROM receipt_line_item as rli '
	                          ' GROUP BY rli.invoice_no ) as li '
			                  ' JOIN invoice as i '
	                          ' ON li."Invoice No" = i.invoice_no '
                              ' JOIN customer as c '
	                          ' ON i.customer_code = c.customer_code) as CD ')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns

    return render(request, 'report_date_amount_received.html', data_report)

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result