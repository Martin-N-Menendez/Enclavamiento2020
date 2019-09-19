----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 08/25/2015 09:06:42 AM
-- Design Name: 
-- Module Name: logic - Behavioral
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity logic is
  Generic (
    Logical_AND : boolean := true;
    Logical_OR : boolean := false;
    Logical_INV : boolean := false;
    DATA_WIDTH    : integer    := 2
  );
  Port (
    --my_AND
    In1 : in std_logic_vector(DATA_WIDTH-1 downto 0);
    In2 : in std_logic_vector(DATA_WIDTH-1 downto 0);
    Out1 : out std_logic_vector(DATA_WIDTH-1 downto 0)
   );
end logic;

architecture Behavioral of logic is

component my_AND is
    generic (
        my_DATA_WIDTH    : integer    := 2
    );
    port (
        In1 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        In2 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        Out1 : out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end component my_AND;
component my_OR is
    generic (
        my_DATA_WIDTH    : integer    := 2
    );
    port (
        In1 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        In2 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        Out1 : out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end component my_OR;

component my_INV is
    generic (
        my_DATA_WIDTH    : integer    := 2
    );
    port (
        In1 : in std_logic_vector(DATA_WIDTH-1 downto 0);
        Out1 : out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end component my_INV;

begin

gen_AND : if Logical_AND  generate
my_AND_inst : my_AND
    generic map (
        my_DATA_WIDTH => DATA_WIDTH
    )
    port map (
            In1 => In1,
            In2 => In2,
            Out1 => Out1
    );
end generate;

gen_OR : if Logical_OR  generate
my_OR_inst : my_OR
    generic map (
        my_DATA_WIDTH => DATA_WIDTH
    )
    port map (
            In1 => In1,
            In2 => In2,
            Out1 => Out1
    );
end generate;

gen_INV : if Logical_INV  generate
my_INV_inst : my_INV
    generic map (
        my_DATA_WIDTH => DATA_WIDTH
    )
    port map (
            In1 => In1,
            Out1 => Out1
    );
end generate;

end Behavioral;
