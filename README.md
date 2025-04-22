# Factory Method
Factory Method define una interfaz para crear objetos, permitiendo que las subclases decidan qué clase concreta instanciar.
De este modo, se delega la creación a clases concretas (creators), lo que permite que el código cliente trabaje solo con interfaces, favoreciendo la extensibilidad y evitando acoplamientos directos con clases concretas.