// Utilidades globales para Alke Wallet

/**
 * Formatea un número como moneda chilena (CLP)
 * Uso: formatCLP(60000) → "$60.000"
 */
function formatCLP(value) {
    return new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
        maximumFractionDigits: 0
    }).format(Number(value) || 0);
}