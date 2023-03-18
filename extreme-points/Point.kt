class Point(val id: String, val x: Float, val y: Float){
	
	
	fun isPointInsideTriangle (triangle: Triangle): Boolean{
		val orientation1 = orientation(triangle.a, triangle.b, this)
		val orientation2 = orientation(triangle.b, triangle.c, this)
		val orientation3 = orientation(triangle.c, triangle.a, this)

		if (orientation1 == Direction.CLOCKWISE
			&& orientation2 == orientation1
			&& orientation3 == orientation2){
			return true
		}
		if (orientation1 == Direction.COUNTERCLOCKWISE
			&& orientation2 == orientation1
			&& orientation3 == orientation2){
			return true
		}
		return false
	}
	
	override fun toString(): String {
		return "$id:$x:$y"
	}

	companion object {
		
		fun orientation (p: Point, q: Point, r: Point): Direction{
			val value = (r.y - p.y) * (q.x - p.x) - (q.y - p.y) * (r.x - p.x)
			if(value == 0f){
				return Direction.COLLINEAR
			} else if(value > 0){
				return Direction.COUNTERCLOCKWISE
			} else return Direction.CLOCKWISE
		}

		fun extremePoints (points: List<Point>): List<Point>{
			var convexHull = mutableListOf<Point>()
			val n = points.size - 1
			for (pointIndex in 0..n){
				var isInside = false

				for (i in 0..n){
					if (i == pointIndex) continue
					
					for (j in (i + 1)..n){
						if(j == pointIndex) continue

						for (k in (j + 1)..n){
							if (k == pointIndex) continue
							val p = points[i]
							val q = points[j]
							val r = points[k]
							val triangle = Triangle(p, q, r)
							val current = points[pointIndex]
							if (current.isPointInsideTriangle(triangle)){
								isInside = true
								break
							}
						}
						if (isInside) break
					}
					if (isInside) break
				}
				if (!isInside)
					convexHull.add(points[pointIndex])
			}
			return convexHull
		}
	}
}
