----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 08/25/2015 10:20:57 AM
-- Design Name: 
-- Module Name: my_AND - Behavioral
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

entity my_inv is
    generic (
        DATA_WIDTH    : integer    := 2
    );
    port (
        In1 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        Out1 : out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end my_INV;

architecture behave of my_INV is
begin

    process(In1)
    begin
        for I in (DATA_WIDTH-1) downto 0 loop
            if ((In1(I)='0')) then
	           Out1(I) <= '1';
	        else
	           Out1(I) <= '0';
	       end if;
	    end loop;
    end process;

end behave;