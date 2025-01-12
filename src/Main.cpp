#include <QApplication>
#include "MainWindow.h"
#include "LoginDialog.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Show the login dialog
    LoginDialog loginDialog;
    if (loginDialog.exec() == QDialog::Accepted) {
        // If login is successful, show the main window with the user role
        MainWindow window(loginDialog.getUserRole());
        window.show();
        return app.exec();
    }

    // If login is not successful, exit the application
    return 0;
}