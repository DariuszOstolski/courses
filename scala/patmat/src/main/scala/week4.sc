object week4 {
	trait List[T] {
		def isEmpty: Boolean
		def head: T
		def tail: List[T]
		}
		
	class Cons[T](val head: T, val tail: List[T]) extends List[T] {
		def isEmpty = false
	}
	
	class Nil[T]	extends List[T] {
		def isEmpty = true
		def head: Nothing = throw new NoSuchElementException("nil.head")
		def tail: Nothing = throw new NoSuchElementException("nil.tail")
	}
	
	object List{
		def List() = new Nil()
		
		def List[T](x: T) = new Cons(x, new Nil)
		def List[T](x: T, y: T): List[T] = new Cons(x, List(y))
		def List[T](x: T, y: T, z: T): List[T] = new Cons(x, List(y,z))
		
	}
  println("Welcome to the Scala worksheet")
  List(1,2,3)
  
}