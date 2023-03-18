# Extreme Points

## Running

Build the executable with:

```bash
	kotlinc *.kt  -cp . -include-runtime -d extreme-points.jar
```

then run:

```bash
	java -jar extreme-points.jar < [POINTS]
```

where:
- `[POINTS]`: It's the file containing the points, whose format is: `id:x-coordinate:y-coordinate`. Each points is separated with a `,`.

The app returns `result.txt` with the `id`'s of the points that belongs to the **Convex Hull.**
