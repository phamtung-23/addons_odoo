/** @odoo-module */

import { registry } from '@web/core/registry';
import { memoize } from '@web/core/utils/functions';
import { session } from "@web/session";

const { reactive } = owl;

export const tshirtService = {
    dependencies: ["rpc", "orm"],
    async start(env, { rpc, orm }) {
        const statistics = reactive({});

        if (session.tshirt_statistics) {
            Object.assign(statistics, session.tshirt_statistics);
        } else {
            Object.assign(statistics, await rpc("/awesome_tshirt/statistics"));
        }

        async function loadCustomers() {
            return await orm.searchRead("res.partner", [], ["display_name"]);
        }

        setInterval(async () => {
            Object.assign(statistics, await rpc("/awesome_tshirt/statistics"));
        }, 30000);
        
        return {
            statistics,
            loadCustomers: memoize(loadCustomers),
        }
    },
}

registry.category("services").add("tshirtService", tshirtService);