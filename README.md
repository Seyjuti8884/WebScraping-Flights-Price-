<!DOCTYPE html>
<html>
  <head>
    <style>
      /* CSS styles for the animation */
      body {
        background-color: #f2f2f2;
        margin: 0;
        padding: 0;
      }

      .frame {
        width: 100%;
        height: auto;
        margin: 15% auto 0;
        position: relative;
      }

      .plane-container {
        width: 200px;
        margin: 0 auto;
        position: relative;
        z-index: 3;
        animation: planeAnimation 5s linear infinite;
      }

      .plane-container a {
        display: block;
        width: 100%;
      }

      .plane {
        width: 100%;
        height: auto;
      }

      .runway {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 20px;
        background-color: #333;
        z-index: 2;
      }

      /* Keyframes for plane animation */
      @keyframes planeAnimation {
        0% {
          transform: translateX(-100%);
        }
        100% {
          transform: translateX(100%);
        }
      }
    </style>
  </head>
  <body>
    <div class="frame">
      <div class="plane-container">
        <a href="http://customer.io/" target="_blank">
          <svg
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            x="0px"
            y="0px"
            width="1131.53px"
            height="379.304px"
            viewBox="0 0 1131.53 379.304"
            enable-background="new 0 0 1131.53 379.304"
            xml:space="preserve"
            class="plane"
          >
            <polygon
              fill="#D8D8D8"
              points="72.008,0 274.113,140.173 274.113,301.804 390.796,221.102 601.682,367.302 1131.53,0.223 "
            />
            <polygon
              fill="#C4C4C3"
              points="1131.53,0.223 274.113,140.173 274.113,301.804 390.796,221.102 "
            />
          </svg>
        </a>
      </div>
      <div class="runway"></div>
    </div>
  </body>
</html>
