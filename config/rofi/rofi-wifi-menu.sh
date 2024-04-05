#!/usr/bin/env bash

# Mensaje de notificación
notify-send "Obteniendo lista de redes Wi-Fi disponibles..."

# Obtener la lista de conexiones Wi-Fi disponibles y darle formato
wifi_list=$(nmcli --fields "SECURITY,SSID" device wifi list | sed 1d | sed 's/  */ /g' | sed -E "s/WPA*.?\S/ /g" | sed "s/^--/ /g" | sed "s/  //g" | sed "/--/d")

# Verificar el estado de la conexión Wi-Fi
connected=$(nmcli -fields WIFI g)
if [[ "$connected" =~ "enabled" ]]; then
    toggle="󰖪  Desactivar Wi-Fi"
elif [[ "$connected" =~ "disabled" ]]; then
    toggle="󰖩  Activar Wi-Fi"
fi

# Utilizar rofi para seleccionar la red Wi-Fi
chosen_network=$(echo -e "$toggle\n$wifi_list" | uniq -u | rofi -dmenu -i -selected-row 1 -p "SSID Wi-Fi: " )
# Obtener el nombre de la conexión
read -r chosen_id <<< "${chosen_network:3}"

if [ "$chosen_network" = "" ]; then
    exit
elif [ "$chosen_network" = "󰖩  Activar Wi-Fi" ]; then
    nmcli radio wifi on
elif [ "$chosen_network" = "󰖪  Desactivar Wi-Fi" ]; then
    nmcli radio wifi off
else
    # Mensaje de éxito
    success_message="Ahora estás conectado a la red Wi-Fi \"$chosen_id\"."
    # Obtener conexiones guardadas
    saved_connections=$(nmcli -g NAME connection)
    if [[ $(echo "$saved_connections" | grep -w "$chosen_id") = "$chosen_id" ]]; then
        nmcli connection up id "$chosen_id" | grep "successfully" && notify-send "Conexión Establecida" "$success_message"
    else
        if [[ "$chosen_network" =~ "" ]]; then
            wifi_password=$(rofi -dmenu -p "Contraseña: " )
        fi
        nmcli device wifi connect "$chosen_id" password "$wifi_password" | grep "successfully" && notify-send "Conexión Establecida" "$success_message"
    fi
fi
