/** @odoo-module **/

const { onMounted, onWillUnmount } = owl;

export function useInterval(func, ms){
    let interval
    onMounted(() => {
        interval = setInterval(func, ms);
    });

    onWillUnmount(() => {
        clearInterval(interval);
    });
}