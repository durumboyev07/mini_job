queue = []

while True:
    print("1.Add 2.Run")
    c = input("> ")

    if c == "1":
        job = input("Job: ")
        queue.append(job)

    elif c == "2":
        if queue:
            print("Running:", queue.pop(0))
