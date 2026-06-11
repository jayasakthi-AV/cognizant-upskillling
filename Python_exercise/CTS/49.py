class Converter:
    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

converter = Converter()

temp = converter.celsius_to_fahrenheit(25)

print(f"Temperature: {temp:.2f} F")