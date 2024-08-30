import { ref } from "vue";

const Breakpoints = {
  XSmall: "(max-width: 599.99px)",
  Small: "(min-width: 600px) and (max-width: 959.99px)",
  Medium: "(min-width: 960px) and (max-width: 1279.99px)",
  Large: "(min-width: 1280px)"
};

let handlers = [];
const xSmallMedia = window.matchMedia(Breakpoints.XSmall);
const smallMedia = window.matchMedia(Breakpoints.Small);
const mediumMedia = window.matchMedia(Breakpoints.Medium);
const largeMedia = window.matchMedia(Breakpoints.Large);

[xSmallMedia, smallMedia, mediumMedia, largeMedia].forEach(media => {
  media.addListener(() => {
    handlers.forEach(handler => handler());
  });
});

export const sizes = () => {
  return {
    "screen-x-small": xSmallMedia.matches,
    "screen-small": smallMedia.matches,
    "screen-medium": mediumMedia.matches,
    "screen-large": largeMedia.matches
  };
};

function getScreenSizeInfo() {
  const screenSizes = sizes();
  return {
    isXSmall: screenSizes['screen-x-small'],
    isSmall: screenSizes['screen-small'],
    isMedium: screenSizes['screen-medium'],
    isLarge: screenSizes['screen-large'],
    cssClasses: Object.keys(screenSizes).filter((cl) => screenSizes[cl]),
  };
}

export const screenInfo = ref(getScreenSizeInfo())

export const subscribe = handler => handlers.push(handler);

export const unsubscribe = handler => {
  handlers = handlers.filter(item => item !== handler);
};