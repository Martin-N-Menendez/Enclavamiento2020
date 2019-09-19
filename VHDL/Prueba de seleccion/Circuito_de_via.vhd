----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 18.09.2019 19:02:59
-- Design Name: 
-- Module Name: Circuito_de_via - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Circuito_de_via is
    Port ( clock : in STD_LOGIC;
           anterior_leer : in STD_LOGIC;
           posterior_leer : in STD_LOGIC;
           anterior_escribir : out STD_LOGIC;
           posterior_escribir : out STD_LOGIC;
           ocupacion : in STD_LOGIC);
end Circuito_de_via;

architecture Behavioral of Circuito_de_via is

begin


end Behavioral;
