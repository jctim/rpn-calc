object rpn {
    def calculate(expression: String): Double = {
        def calc(stack: List[Double], token: String): List[Double] = {
            (token, stack) match {
                case ("+", h1 :: h2 :: rest) => (h2 + h1) :: rest
                case ("-", h1 :: h2 :: rest) => (h2 - h1) :: rest
                case ("*", h1 :: h2 :: rest) => (h2 * h1) :: rest
                case ("/", h1 :: h2 :: rest) => (h2 / h1) :: rest
                case ("^", h1 :: h2 :: rest) => (Math.pow(h2,h1)) :: rest
                case (t, s) => t.toDouble :: s
            }
        }

        val tokens = expression.split(" ").toList
        val res = tokens.foldLeft(List[Double]()) { case (stack, t) => calc(stack, t)}
        return res.head
        
    }
}