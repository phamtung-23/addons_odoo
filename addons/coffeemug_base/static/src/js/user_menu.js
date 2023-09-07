/** @odoo-module **/
import { registry } from "@web/core/registry";
import { preferencesItem } from "@web/webclient/user_menu/user_menu_items";
import { routeToUrl } from "@web/core/browser/router_service";
import { browser } from "@web/core/browser/browser";
const userMenuRegistry = registry.category("user_menuitems");

function debugItem(env) {
   const debugURL = $.param.querystring(window.location.href, 'debug=1');
   return {
       type: "item",
       id: "debug",
       description: env._t("Activate the developer mode"),
       href: debugURL,
       callback: () => {
           browser.open(debugURL, "_self");
       },
       sequence: 50,
   };
}

function removeMenuItem(menuItemId) {
    userMenuRegistry.remove(menuItemId);
}

removeMenuItem('odoo_account')
removeMenuItem('documentation')
removeMenuItem('support')

registry.category("user_menuitems").add("debug", debugItem)








