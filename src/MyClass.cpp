// MyClass.cpp
#include "MyClass.h"
#include <QDebug>

void MyClass::someMethod() {
    qDebug() << "Entering someMethod";
    // Method logic here
    qDebug() << "Exiting someMethod";
}