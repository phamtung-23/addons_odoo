var SwitchCompanyMenu = document.querySelector(".oe_topbar_name");

if (SwitchCompanyMenu) {
    SwitchCompanyMenu.textContent = SwitchCompanyMenu.textContent.replace("(odoo)", "");
}