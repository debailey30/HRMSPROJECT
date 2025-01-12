#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "UserRoles.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(UserRole role, QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    UserRole userRole;
};

#endif // MAINWINDOW_H
