#include "stm32f1xx_hal.h"  // Inclusion de la bibliothèque HAL pour le STM32

#define FULL_CAPACITY 10000  // Capacité totale de la batterie en mAh

ADC_HandleTypeDef hadc1;  // Déclaration de la structure de gestion de l'ADC1
ADC_HandleTypeDef hadc2;  // Déclaration de la structure de gestion de l'ADC2

float current_charge = 0.0;  // Variable pour stocker le courant de charge en mA
float current_discharge = 0.0;  // Variable pour stocker le courant de décharge en mA
float charge = FULL_CAPACITY * 0.5;  // Par exemple, 50 % de charge initiale en mAh
float soc = 50.0;  // État de charge initial en pourcentage

void SystemClock_Config(void);  // Prototype de la fonction de configuration de l'horloge système
void MX_GPIO_Init(void);  // Prototype de la fonction d'initialisation des GPIO
void MX_ADC1_Init(void);  // Prototype de la fonction d'initialisation de l'ADC1
void MX_ADC2_Init(void);  // Prototype de la fonction d'initialisation de l'ADC2

int main(void)
{
    HAL_Init();  // Initialisation de la bibliothèque HAL
    SystemClock_Config();  // Configuration de l'horloge système
    MX_GPIO_Init();  // Initialisation des GPIO
    MX_ADC1_Init();  // Initialisation de l'ADC1
    MX_ADC2_Init();  // Initialisation de l'ADC2

    while (1)
    {
        // Lire le courant de charge de la batterie
        HAL_ADC_Start(&hadc1);  // Démarrer la conversion ADC1
        if (HAL_ADC_PollForConversion(&hadc1, 100) == HAL_OK)  // Attendre la fin de la conversion
        {
            current_charge = HAL_ADC_GetValue(&hadc1);  // Obtenir la valeur convertie (courant de charge en mA)
        }
        HAL_ADC_Stop(&hadc1);  // Arrêter la conversion ADC1

        // Lire le courant de décharge de la batterie
        HAL_ADC_Start(&hadc2);  // Démarrer la conversion ADC2
        if (HAL_ADC_PollForConversion(&hadc2, 100) == HAL_OK)  // Attendre la fin de la conversion
        {
            current_discharge = HAL_ADC_GetValue(&hadc2);  // Obtenir la valeur convertie (courant de décharge en mA)
        }
        HAL_ADC_Stop(&hadc2);  // Arrêter la conversion ADC2

        // Calculer l'état de charge (SoC)
        charge += (current_charge - current_discharge) / 3600.0;  // Intégration des courants sur 1 seconde (1 heure = 3600 secondes)
        soc = (charge / FULL_CAPACITY) * 100;  // Calculer le SoC en pourcentage

        // Vérifier les limites de l'état de charge
        if (soc > 100.0)
            soc = 100.0;  // Limiter le SoC à 100 % maximum
        if (soc < 0.0)
            soc = 0.0;  // Limiter le SoC à 0 % minimum

        // Afficher le SoC
        printf("State of Charge (SoC): %.2f%%\n", soc);  // Afficher l'état de charge en pourcentage

        HAL_Delay(1000);  // Attendre 1 seconde avant la prochaine mesure
    }
}

// Initialisation des ADC, GPIO et horloge
void SystemClock_Config(void) { /* Configuration de l'horloge */ }
void MX_GPIO_Init(void) { /* Initialisation des GPIO */ }
void MX_ADC1_Init(void) { /* Configuration de l'ADC1 */ }
void MX_ADC2_Init(void) { /* Configuration de l'ADC2 */ }
