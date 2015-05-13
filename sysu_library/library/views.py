from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from library.models import *
# from library.courseCrawler import getBooksByCourse
# from library.bookCrawler import getBooksListByName

def searchByCourse(requset):
	if requset.method == 'GET':
		course = requset.GET["course"]
		try:
			# check whether this couse is in database
			c = Course.objects.get(cname = course)
			# return the historic result
			return getExistCourseRecord(c)
		except Course.DoesNotExist:
			booksNames = getBooksByCourse(course)
			if not len(booksNames):
				return HttpResponse("No correlated book")

# service for function searchByCourse
def getExistCourseRecord(course_object):
	relations = c.relation_set.all()
	bookids = [r.bid for r in relations]
	xml = '''<?xml version="1.0" encoding="UTF-8"?>\n'''
	xml += '''<bookList>\n'''
	for bookid in bookids:
		xml += getBookItemXml(bookid)
	xml += '''</bookList>'''

# create a xml for a book
def getBookItemXml(bookid):
	try:
		b = Books.objects.get(id = bookid)
	except Books.DoesNotExist:
		return ""
	        <name>书名</name>
        <pic>封面图url</pic>
        <author>作者</author>
        <publisher>出版社</publisher>
        <num>索书号</num>
        <av>是否可借(0或1</av>
        <detail>详情页面url的id</detail>
	item_xml = '<item>\n' +\
	           '<name>%s</name>\n' +\
	           '<pic>%s</pic>\n' +\
	           '<author>%s</author>\n' +\
	           '<publisher>%s</publisher>\n' +\
               '<num>%s</num>\n' +\
               '<detail>%s</detail>\n' +\
               '</item>\n'

def getExistBookRecord():

def searchByBook(requset):
	pass

def getBookDetail(requset):
	pass

def clickIncrement(requset):
	pass