import java.io.File

fun stringToPoint(point: String): Point{
	val data = point.split(":")
	val x = data[1].toFloat()
	val y = data[2].toFloat()

	return Point(data[0], x, y) 
}


fun main() {
	val data = generateSequence(::readLine)
				.toList()
	
	val points = data[0].split(",").map { stringToPoint(it) }
	
	val result = Point.extremePoints(points)
					.map{ it.id }
					.joinToString("\n")
	
	File("solution.txt").writeText(result)

}

