object GetFloor {
    def main(args: Array[String]) {
      
    	val source = scala.io.Source.fromFile("input.txt")
		val lines = try source.mkString finally source.close()
        println(lines)
    }
}