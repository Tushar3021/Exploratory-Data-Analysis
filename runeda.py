import streamlit as st

class RunEDA:

	def __init__(self):
		self.apps = []

	def add_app(self, title, func):
		self.apps.append({
			"title": title,
			"function": func
		})

	def run(self):
		app = st.sidebar.radio(
			'Start',
			self.apps,
			format_func=lambda app: app['title'])

		app['function']()