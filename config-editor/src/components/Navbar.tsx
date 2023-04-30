import {
  Box,
  Flex,
  Button,
  useColorModeValue,
  Stack,
  useColorMode,
  Text
} from "@chakra-ui/react";
import { MoonIcon, SunIcon, SettingsIcon } from "@chakra-ui/icons";

export default function Nav() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <>
      <Box bg={useColorModeValue("gray.100", "gray.900")} px={4}>
        <Flex h={"10vh"} alignItems={"center"} justifyContent={"space-between"}>
          <Text>XTouch Mini Eos</Text>

          <Flex alignItems={"center"}>
            <Stack direction={"row"} spacing={2} alignItems="center">
              <Button onClick={toggleColorMode} size={"sm"}>
                {colorMode === "light" ? <MoonIcon /> : <SunIcon />}
              </Button>
              <Button onClick={() => console.log("menu")} size={"sm"}>
                <SettingsIcon /> {/* Add Model for Settings */}
              </Button>
            </Stack>
          </Flex>
        </Flex>
      </Box>
    </>
  );
}
