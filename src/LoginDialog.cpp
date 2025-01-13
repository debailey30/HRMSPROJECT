#include <QDialog>
#include "UserRoles.h"

namespace Ui {
/// @brief 
class LoginDialog;
}

class LoginDialog : public QDialog {
    Q_OBJECT

public:
    explicit LoginDialog(QWidget *parent = nullptr);
    ~LoginDialog();
    UserRole getUserRole() const;

private slots:
    void on_loginButton_clicked();
    void on_forgotUsernameButton_clicked(); // Slot for "Forgot Username" button

private:
    Ui::LoginDialog *ui;
    UserRole userRole;
};

#include "LoginDialog.h"
#include "ui_LoginDialog.h"
#include <QMessageBox> // Include for message box

LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this);
}

LoginDialog::~LoginDialog() {
    delete ui;
}

UserRole LoginDialog::getUserRole() const {
    return userRole;
}

void LoginDialog::on_loginButton_clicked() {
    // Handle login button click
}

void LoginDialog::on_forgotUsernameButton_clicked() {
    // Handle forgot username button click
}