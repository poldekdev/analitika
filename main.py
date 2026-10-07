import src.analitika.charts.bar


fig, ax = src.analitika.charts.bar.generate_chart(["A", "B", "C"], [1, 2, 3], "Test")

fig.savefig("image.png")
