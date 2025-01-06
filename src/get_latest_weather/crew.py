from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.weather_tool import weather_tool
from .tools.geocoding_tool import geocoding_tool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class GetLatestWeather():
	"""GetLatestWeather crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def geocoding_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['geocoding_expert'],
			tools=[geocoding_tool],
			verbose=True
		)

	@agent
	def weather_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['weather_expert'],
			tools=[weather_tool],
			verbose=True
		)

	@task
	def get_city_coordinates_task(self) -> Task:
		return Task(
			config=self.tasks_config['get_city_coordinates_task']
		)

	@task
	def get_latest_weather_task(self) -> Task:
		return Task(
			config=self.tasks_config['get_latest_weather_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the GetLatestWeather crew"""
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
			tasks=self.tasks,  # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True
		)
