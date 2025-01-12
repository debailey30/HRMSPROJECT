#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(UserRole role, QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    userRole(role)
{
    ui->setupUi(this);

    if (userRole == Manager) {
        // Show manager-specific features
    } else {
        // Show employee-specific features
    }
}

MainWindow::~MainWindow() {
    delete ui;
}