import { Select, Square, Text, VStack } from "@chakra-ui/react";

export default function MidiButton(props: {
  buttonNum: number;
  layer: string;
}) {
  let bNum = props.buttonNum;
  // if (props.layer === "B") {
  //   bNum = bNum + 16;
  // }
  return (
    <VStack>
      <Square size="12" bg="teal">
        <Text>B{bNum}</Text>
      </Square>
      <Select placeholder="Press Action" size={"xs"}>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </Select>
    </VStack>
  );
}
