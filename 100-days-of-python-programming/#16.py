def fruit_color(fruit):
    match fruit:
        case "apple":
            return "red"
        case "banana":
            return "yellow"
        case "grape":
            return "purple"
        case _:
            return "unknown"

result = fruit_color("banana")
print(result)  # Output will be "yellow"
