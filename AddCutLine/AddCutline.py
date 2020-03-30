import sublime
import sublime_plugin
import re
import math

class AddcutlineCommand(sublime_plugin.TextCommand):
	def run(self, edit,LEN=""):
		region = self.view.sel()[0]       #获取当前选取的区域，a = self.view.sel()[0].a 获取当前区域的起始point 
		region = self.view.line(region)   #获取当前整行
		str_a = self.view.substr(region)  #获取当前选择区域字符串
		parameter = sublime.load_settings("AddCutLine.sublime-settings")
		if (LEN== ""):
			LEN = parameter.get('LEN')
		print(LEN)
		if len(str_a)==0:                 #如果仅是光标的位置，从该位置的那一行顶行插入cutline
			region=self.view.line(region) #获取从行开始的region
			point = region.a
			if LEN == "long":
				self.view.insert(edit, point, "//=======================================================================================================================================================\n")      #打印时显示在最底下
				self.view.insert(edit, point, "//---------------------------------------------------------------------- Text Here ----------------------------------------------------------------------\n")
				self.view.insert(edit, point, "//=======================================================================================================================================================\n") 
			elif LEN == "short":
				self.view.insert(edit, point, "//===========================================================================\n")      #打印时显示在最底下
				self.view.insert(edit, point, "//-------------------------------- Text Here --------------------------------\n")
				self.view.insert(edit, point, "//===========================================================================\n")
		else:
			print(str_a)
			region=self.view.line(region)
			point = region.a
			print(region)
			str_a = self.view.substr(region)
			print(str_a)
			str = re.findall(r"\s*[/#]+\s*(.*\S+)\s*$", str_a)  #取得//或者#后面的字符串，去除前后空格
			srt_len =len(str[0]) 
			print(srt_len)
			print(str)

			if LEN == "short":
				self.view.erase(edit,region)
				self.view.insert(edit, point, "//===========================================================================\n")      #打印时显示在最底下
				self.view.insert(edit, point, "//---------------------------------------------------------------------------\n")
				self.view.insert(edit, point, "//===========================================================================\n")
	
				first_line_end = self.view.line(point).b #获取当前行的region (1739, 1816) 起始point
	
				print(first_line_end)
				#计算替换字符串的偏移量
				start_p = first_line_end+round((75-srt_len)/2)+3
				r1 = sublime.Region(start_p,start_p+srt_len) 
				print(round((75-srt_len)/2))
				self.view.replace(edit, r1, str[0])           #将该区域替换为原来的注释
			elif LEN == "long":
				self.view.erase(edit,region)
				self.view.insert(edit, point, "//=======================================================================================================================================================\n")      #打印时显示在最底下
				self.view.insert(edit, point, "//-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
				self.view.insert(edit, point, "//=======================================================================================================================================================\n") 
	
				first_line_end = self.view.line(point).b #获取当前行的region (1739, 1816) 起始point
	
				print(first_line_end)
				#计算替换字符串的偏移量
				start_p = first_line_end+round((151-srt_len)/2)+3
				r1 = sublime.Region(start_p,start_p+srt_len) 
				print(round((151-srt_len)/2))
				self.view.replace(edit, r1, str[0])           #将该区域替换为原来的注释
