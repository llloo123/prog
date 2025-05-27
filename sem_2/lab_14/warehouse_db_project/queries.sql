CREATE DATABASE warehouse_db;
USE warehouse_db;

-- Создание таблицы Поставщики
CREATE TABLE Suppliers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company VARCHAR(100) NOT NULL,
    contact VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);

-- Создание таблицы Товары
CREATE TABLE Products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы Заказы
CREATE TABLE Orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    supplier_id INT NOT NULL,
    order_date DATE NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
);
