def eat(number, need, remaining):
    total_eaten = number + min(need, remaining)
    remaining -= min(need, remaining)
    return [total_eaten, remaining]